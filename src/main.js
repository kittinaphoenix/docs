var dark_mode = false;

var menuAccordion;
var containerContent;
var toggleSwitch;

document.addEventListener("DOMContentLoaded", function () {
  toggleSwitch = document.querySelector('#dark-mode-switch');
  toggleSwitch.addEventListener('change', switchTheme, false);

  if (dark_mode) {
    toggleSwitch.checked = true;
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    toggleSwitch.checked = false;
    document.documentElement.setAttribute('data-theme', 'light');
  }

  menuAccordion = document.getElementById('left-menu');
  containerContent = document.getElementById("content-container");
  populateMenu();
  loadContent("sections/home.html")
});

function switchTheme(event) {
  if (event.target.checked) {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }
}

function populateMenu() {
  fetch('sections.json')
  .then(response => response.json())
  .then(sections => {
    const menuHTML = generateMenu(sections);
    menuAccordion.innerHTML = menuHTML;
  })
  .catch(error => console.error(error));
}

function generateMenu(items, level = 0) {
  let menuHTML = '<ul>';
  let backgroundColor = `rgba(0, 0, 0, ${level * 0.1})`;
  let paddingLeft = 5 + level * 10;

  items.forEach((item) => {
    switch (item.type) {
      case 'group':
        menuHTML += `<li class="li-tree-custom" style="background-color: ${backgroundColor}">
        <input type="checkbox" id="${item.label.replace(/ /g, '-')}" hidden onclick="toggleArrowRotation(this)" />
        <label class="li-tree-label-custom" for="${item.label.replace(/ /g, '-')}" style="padding-left: ${paddingLeft + 3}px">${item.label}<span class="arrow-container"><i class="fa fa-chevron-right" aria-hidden="true"></i></span></label>
        ${generateMenu(item.group, level + 1)}
        </li>`
        break;
      case 'section':
        menuHTML += `<li class="li-direct-custom" style="background-color: ${backgroundColor}"><a class="li-btn-custom" href="#" onclick="loadContent('${item.url}');" style="padding-left: ${paddingLeft}px">${item.label}</a></li>`;
        break;
    }
  });
  menuHTML += '</ul>';
  return menuHTML;
}

function toggleArrowRotation(element) {
  const arrowContainer = element.parentElement.querySelector(".arrow-container");
  arrowContainer.classList.toggle("arrow-rotate");
}

function loadContent(url) {
  fetch(url)
    .then(response => response.text())
    .then(html => {
      const wrapper = document.createElement('div');
      wrapper.innerHTML = html;
      containerContent.innerHTML = html;
      hljs.highlightAll();
    })
    .catch(error => {
      console.error(error);
    });
}