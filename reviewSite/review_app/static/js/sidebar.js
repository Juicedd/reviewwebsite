document.addEventListener('DOMContentLoaded', function() {
    // Get the sidebar toggle button
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.getElementById('sidebarMenu');
    
    // Add click event to toggle the icon
    if (sidebarToggle) {
      sidebarToggle.addEventListener('click', function() {
        // Toggle the icon between left and right arrow
        const icon = this.querySelector('i');
        
        // Wait for the collapse animation to complete
        setTimeout(function() {
          if (sidebar.classList.contains('show')) {
            icon.classList.remove('bi-arrow-right-circle');
            icon.classList.add('bi-arrow-left-circle');
          } else {
            icon.classList.remove('bi-arrow-left-circle');
            icon.classList.add('bi-arrow-right-circle');
          }
        }, 350); // Bootstrap collapse animation takes ~350ms
      });
    }
    
    // Handle initial state
    function checkSidebarState() {
      if (window.innerWidth < 768) {
        sidebar.classList.remove('show');
      } else {
        sidebar.classList.add('show');
      }
    }
    
    // Check initial state
    checkSidebarState();
    
    // Check on window resize
    window.addEventListener('resize', checkSidebarState);
  });