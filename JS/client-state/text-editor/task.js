const editor = document.getElementById('editor');
const clearBtn = document.getElementById('clearBtn');

function saveText() {
    localStorage.setItem('editorContent', editor.value);
}

function loadText() {
    const savedText = localStorage.getItem('editorContent');
    if (savedText) {
        editor.value = savedText;
    }
}

function clearContent() {
    editor.value = '';
    localStorage.removeItem('editorContent');
}

editor.addEventListener('input', saveText);

clearBtn.addEventListener('click', clearContent);

window.addEventListener('load', loadText);
