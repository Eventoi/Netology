document.addEventListener('DOMContentLoaded', function() {

  const tooltipElements = document.querySelectorAll('.has-tooltip');

  tooltipElements.forEach(function(element) {

    const tooltip = document.querySelector('.tooltip');

    element.addEventListener('click', function(event) {
      event.preventDefault();
      const tooltipText = element.getAttribute('title');
      tooltip.textContent = tooltipText;
      const rect = element.getBoundingClientRect();
      tooltip.style.top = rect.bottom + 5 + 'px';
      tooltip.style.left = rect.left + 'px';


      tooltip.classList.add('tooltip_active');
      

      document.addEventListener('click', function closeTooltip(event) {
        if (!element.contains(event.target)) {
          tooltip.classList.remove('tooltip_active');
          document.removeEventListener('click', closeTooltip);
        }
      });
    });
  });
});
