// Dashboard

const project_info = document.getElementById('project-info');
const expand_toggle = document.getElementById('expand-toggle');

expand_toggle.addEventListener('click', () => {
    if (project_info.className.includes('active')){
        project_info.style.display = 'none';
        project_info.className -= 'active';

    } else {
        project_info.style.display = 'block';
        project_info.className += 'active';
    }

})