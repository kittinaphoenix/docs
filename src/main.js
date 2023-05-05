var menuAccordion;
var containerContent;

document.addEventListener("DOMContentLoaded", function () {
  const toggleSwitch = document.querySelector('#dark-mode-switch');
  toggleSwitch.addEventListener('change', switchTheme, false);

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
  const menuHTML = generateMenu(sections);
  menuAccordion.innerHTML = menuHTML;
}

function populateMenu() {
  const menuHTML = generateMenu(sections, 0);
  menuAccordion.innerHTML = menuHTML;
}

function generateMenu(items, level) {
  let menuHTML = '<ul>';
  let backgroundColor = `rgba(0, 0, 0, ${level * 0.1})`;
  let paddingLeft = 5 + level * 10;

  items.forEach((item) => {
    if (item.type === 'tree') {
      menuHTML += `<li class="li-tree-custom" style="background-color: ${backgroundColor}">
        <input type="checkbox" id="${item.label.replace(/ /g, '-')}" hidden onclick="toggleArrowRotation(this)" />
        <label class="li-tree-label-custom" for="${item.label.replace(/ /g, '-')}" style="padding-left: ${paddingLeft + 3}px">${item.label}<span class="arrow-container"><i class="fa fa-chevron-right" aria-hidden="true"></i></span></label>
        ${generateMenu(item.tree, level + 1)}
      </li>`;
    } else {
      menuHTML += `<li class="li-direct-custom" style="background-color: ${backgroundColor}"><a class="li-btn-custom" href="#" onclick="loadContent('${item.url}');" style="padding-left: ${paddingLeft}px">${item.label}</a></li>`;
    }
  });
  menuHTML += '</ul>';
  return menuHTML;
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
function toggleArrowRotation(element) {
  //const arrowContainer = element.parentElement.querySelector(".arrow-container");
  //arrowContainer.classList.toggle("arrow-rotate");
}