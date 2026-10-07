// `EP-028·HU-006` · La tabla avanzada de Tabler (List.js, que trae la plantilla), igual que en scilit
// (static/js/main.js). Guía de diseño de pantallas, §6 y §12: un solo código para todas las tablas.
//
// La caja lleva id y data-tabla-avanzada; data-por-pagina dice cuántas filas muestra al empezar
// (0: sin paginar, para las tablas que ya pagina la base). Los títulos son botones
// .table-sort[data-sort="campo"]; cada celda lleva la clase de su campo; los filtros de
// cada columna son [data-filtro="campo"], y con data-exacto son una lista con los valores de la tabla.
document.querySelectorAll('[data-tabla-avanzada]').forEach(caja => {
  if (typeof List === 'undefined') return;
  const id = caja.id;
  const campos = [...caja.querySelectorAll('.table-sort[data-sort]')].map(b => b.dataset.sort);
  const porPagina = parseInt(caja.dataset.porPagina, 10);
  const opciones = {sortClass: 'table-sort', listClass: 'table-tbody', valueNames: campos};
  if (porPagina > 0) {
    opciones.page = porPagina;
    opciones.pagination = {
      item: valor => `<li class="page-item"><a class="page-link cursor-pointer">${valor.page}</a></li>`,
      innerWindow: 1, outerWindow: 1, left: 0, right: 0,
    };
  }
  const lista = new List(id, opciones);
  const filtros = [...caja.querySelectorAll('[data-filtro]')];
  const texto = (item, campo) => (item.elm.querySelector('.' + campo)?.textContent || '').trim();
  filtros.filter(f => f.hasAttribute('data-exacto')).forEach(f => {
    const campo = f.dataset.filtro;
    [...new Set(lista.items.map(item => texto(item, campo)))].filter(Boolean).sort()
      .forEach(valor => f.add(new Option(valor, valor)));
  });
  const vacio = caja.querySelector('[data-sin-coincidencias]');
  const filtrar = () => {
    const activos = filtros.filter(f => f.value.trim());
    if (!activos.length) { lista.filter(); }
    else {
      lista.filter(item => activos.every(f => f.hasAttribute('data-exacto')
        ? texto(item, f.dataset.filtro) === f.value
        : texto(item, f.dataset.filtro).toLowerCase().includes(f.value.trim().toLowerCase())));
    }
    if (vacio) { vacio.hidden = lista.matchingItems.length > 0; }
  };
  filtros.forEach(f => f.addEventListener(f.tagName === 'SELECT' ? 'change' : 'input', filtrar));
  document.querySelectorAll(`[data-tabla="${id}"] [data-filas]`).forEach(boton => {
    boton.addEventListener('click', () => {
      lista.page = parseInt(boton.dataset.filas, 10);
      lista.update();
      document.querySelector(`#${id}-filas`).textContent = boton.dataset.filas;
    });
  });
});
