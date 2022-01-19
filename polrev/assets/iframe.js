import 'iframe-resizer'

document.addEventListener('DOMContentLoaded', function() {
    const iframeEl = document.getElementById('iframe');
    iframeEl.addEventListener("load", () => {
        iFrameResize({ log: true, checkOrigin:false }, iframeEl)
      });
  });