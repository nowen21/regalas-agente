// `EP-025·HU-018` · La ayuda de Cimiento, traída de scilit (EP-014 HU-005).

// El panel de la derecha trae la sección del manual de la pantalla actual
const contenidoAyuda = document.getElementById('ayuda-contenido');
function cargarAyuda(url) {
  if (!contenidoAyuda) return;
  fetch(url, { credentials: 'same-origin' })
    .then(r => { if (!r.ok) throw new Error(r.status); return r.text(); })
    .then(html => { contenidoAyuda.innerHTML = html; })
    .catch(() => {
      contenidoAyuda.innerHTML = '<div class="alert alert-danger">No se pudo cargar la ayuda. Abrir el <a href="/ayuda/">manual completo</a>.</div>';
    });
}
document.querySelectorAll('[data-ayuda-url]').forEach(boton => {
  boton.addEventListener('click', () => cargarAyuda(boton.dataset.ayudaUrl));
});
if (contenidoAyuda) {
  contenidoAyuda.addEventListener('click', e => {
    const enlace = e.target.closest('[data-ayuda-enlace]');
    if (!enlace) return;
    e.preventDefault();
    cargarAyuda(enlace.href);
  });
}

// La ayuda de cada campo: activa los globos (popover) del «?» y los textos emergentes (tooltip)
function activarAyudaDeCampos(raiz = document) {
  if (typeof bootstrap === 'undefined') return;
  raiz.querySelectorAll('[data-bs-toggle="popover"]').forEach(el => bootstrap.Popover.getOrCreateInstance(el));
  raiz.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => bootstrap.Tooltip.getOrCreateInstance(el));
}
window.addEventListener('load', () => activarAyudaDeCampos());

// `EP-028·HU-007`, fase B · Lo que llega por htmx (las pestañas del gasto) trae sus «?»: se activan al llegar,
// y los globos de lo que se va se cierran antes, para que no queden flotando sin su «?».
document.addEventListener('htmx:load', e => activarAyudaDeCampos(e.target));
document.addEventListener('htmx:beforeSwap', e => {
  if (typeof bootstrap === 'undefined' || !e.detail.target) return;
  e.detail.target.querySelectorAll('[data-bs-toggle="popover"]').forEach(el => bootstrap.Popover.getInstance(el)?.dispose());
});

// En pantallas táctiles el «?» no recibe el foco solo: al tocarlo se le da, y el globo abre
document.addEventListener('click', e => {
  const icono = e.target.closest('.ayuda-icono[data-bs-toggle="popover"]');
  if (icono) icono.focus();
});

// Esc cierra todos los globos abiertos
document.addEventListener('keydown', e => {
  if (e.key !== 'Escape' || typeof bootstrap === 'undefined') return;
  document.querySelectorAll('[data-bs-toggle="popover"]').forEach(el => bootstrap.Popover.getInstance(el)?.hide());
});

// «Ver en el manual» desde una ventana de ayuda: cierra la ventana y abre el panel derecho en esa sección
document.querySelectorAll('[data-ayuda-manual]').forEach(boton => {
  boton.addEventListener('click', () => {
    if (typeof bootstrap === 'undefined') return;
    bootstrap.Modal.getInstance(boton.closest('.modal'))?.hide();
    bootstrap.Offcanvas.getOrCreateInstance(document.getElementById('ayuda')).show();
    cargarAyuda(boton.dataset.ayudaManual);
  });
});

// El mapa animado de «Cómo encaja en el sistema»: arranca cada vez que se abre la ventana y con «Reiniciar animación»
function reiniciarMapa(ventana) {
  const mapa = ventana && ventana.querySelector('.mapa');
  if (!mapa) return;
  mapa.classList.remove('mapa-animar');
  void mapa.offsetWidth;  // obliga al navegador a soltar la animación anterior antes de volver a empezar
  mapa.classList.add('mapa-animar');
}
document.querySelectorAll('.modal').forEach(ventana => {
  if (ventana.querySelector('.mapa')) ventana.addEventListener('shown.bs.modal', () => reiniciarMapa(ventana));
});
document.querySelectorAll('[data-mapa-reiniciar]').forEach(boton => {
  boton.addEventListener('click', () => reiniciarMapa(boton.closest('.modal')));
});
