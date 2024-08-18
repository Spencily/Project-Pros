// Dashboard

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

const project_info = document.getElementsByClassName('project-info');
const expand_toggle = document.getElementById('expand-toggle');

expand_toggle.addEventListener('click', () => {

    for (let i = 0; i < project_info.length; i++) {
        if (project_info[i].style.display == 'none') {
            project_info[i].style.display = 'block';
        } else {
            project_info[i].style.display = 'none';
        }
    }
})