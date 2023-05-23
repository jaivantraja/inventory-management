document.addEventListener('DOMContentLoaded', function() {
  var openFormBtn = document.querySelector('.purchase-btn');
  var closeFormBtn = document.querySelector('.close-form-btn');
  var formContainer = document.querySelector('.popup-form-container');

  openFormBtn.addEventListener('click', function() {
    formContainer.classList.add('active');
  });

  closeFormBtn.addEventListener('click', function() {
    formContainer.classList.remove('active');
  });
});
document.addEventListener('DOMContentLoaded', function() {
  var openFormBtn = document.querySelector('.sales-btn');
  var closeFormBtn = document.querySelector('.close-form-btn');
  var formContainer = document.querySelector('.popup-form-container');

  openFormBtn.addEventListener('click', function() {
    formContainer.classList.add('active');
  });

  closeFormBtn.addEventListener('click', function() {
    formContainer.classList.remove('active');
  });
});