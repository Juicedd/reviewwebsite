// Mobile Sidebar Function
function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('show_aside');
  document.getElementById('burger').classList.toggle('clicked');
}

// Web sidebar Function
document.addEventListener("DOMContentLoaded", () => {
  loadSidebarState();
  const toggle = document.getElementById('sidebarToggle');
  toggle.addEventListener("click", () => {
    const currentState = sessionStorage.getItem("sidebarState")
    console.log("current State:" + currentState);
    if (currentState) {
      const newState = currentState === "open" ? "minimized" : "open";
      saveSidebarState(newState);
    } else {
      saveSidebarState("minimized");
    }
    toggleSidebar();
  });
});

function saveSidebarState(state) {
  console.log("saving state: " + state);
  sessionStorage.setItem("sidebarState", state)
}

function loadSidebarState() {
  const state = sessionStorage.getItem("sidebarState");
  if (state === 'minimized') {
    toggleSidebar(); // Default is open
  }
}

function toggleSidebar() {
  let items = document.getElementsByClassName('sidebar_nav_item');
  for (let index = 0; index < items.length; index++) {
    items[index].classList.toggle('minimized');
  }
  document.getElementById('layout').classList.toggle('minimized');
  document.getElementById('sidebarHeader').classList.toggle('minimized');

  document.getElementById('sidebarToggle').classList.toggle('bi-arrows-collapse-vertical');
  document.getElementById('sidebarToggle').classList.toggle('bi-arrows-expand-vertical');
}