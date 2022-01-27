function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

class CampaignPreviewHandler {
    constructor(form, button) {
        this.form = form;
        this.button = button;
        this.previewURL = button.dataset['action'];
        this.previewFrame = document.querySelector('.campaign-admin__preview-frame');
        this.setupListeners();

        if (this.previewURL.includes('edit')) {
            this.showPreview();
        } else {
            this.previewFrame.srcdoc = `
            <html>
            </html >
                <body>
                    <div style='text-align: center; width: 100%;'>
                        <h3>Click 'Reload preview' to load preview</h3>
                    </div>
                </body>
            `
        }
    }

    setupListeners() {
        this.button.addEventListener('click', (e) => {
            e.preventDefault();
            this.button.classList.remove('icon-view');
            this.button.classList.add('icon-spinner');
            this.button.disabled = true;
            this.showPreview();
        });
    }

    showPreview() {
        const formData = new FormData(this.form);
        fetch(this.previewURL, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: formData
        })
            .then(response => response.json())
            .then(responseJSON => {
                if (responseJSON.success) {
                    this.previewFrame.srcdoc = responseJSON.preview;
                } else {
                    // Submit form so user can see errors
                    this.form.submit();
                }
                this.resetButton();
            })
    }

    resetButton() {
        this.button.classList.remove('icon-spinner');
        this.button.classList.add('icon-view');
        this.button.disabled = false;
    }
}


document.addEventListener('DOMContentLoaded', _ => {
    form = document.querySelector('.content form'); // not the best selector
    button = document.querySelector('.campaign-preview');
    if (form && button) {
        new CampaignPreviewHandler(form, button);
    }
});