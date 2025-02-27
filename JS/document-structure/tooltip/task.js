document.addEventListener('DOMContentLoaded', function() {
  const tooltipElements = document.querySelectorAll('.has-tooltip');
  
  tooltipElements.forEach(function(element) {

    element.addEventListener('click', function(event) {
      event.preventDefault();

      const tooltip = document.createElement('div');
      tooltip.classList.add('tooltip');
      const tooltipText = element.getAttribute('title');
      tooltip.innerHTML = `${tooltipText} <a href="#" class="task__remove">&times;</a>`;

      document.body.appendChild(tooltip);

      const rect = element.getBoundingClientRect();
      tooltip.style.top = rect.bottom + 5 + 'px';
      tooltip.style.left = rect.left + 'px';

      tooltip.classList.add('tooltip_active');

      const closeButton = tooltip.querySelector('.task__remove');
      closeButton.addEventListener('click', function() {
        tooltip.classList.remove('tooltip_active');
        tooltip.remove();
      });

      document.addEventListener('click', function closeTooltip(event) {
        if (!element.contains(event.target) && !tooltip.contains(event.target)) {
          tooltip.classList.remove('tooltip_active');
          tooltip.remove();
          document.removeEventListener('click', closeTooltip);
        }
      });
    });
  });
});
