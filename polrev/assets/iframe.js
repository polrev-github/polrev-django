import 'iframe-resizer'
import 'iframe-resizer/js/iframeResizer.contentWindow'

document.addEventListener('DOMContentLoaded', function() {
    const iframeEl = document.getElementById('iframe');
    iframeEl.addEventListener("load", () => {
        iFrameResize({ log: true, checkOrigin:false }, iframeEl)
      });
  });