const openmenu = () => {
    var x = document.getElementById('menu');
    var y = document.getElementById('icon');
    if (x.style.right == '-100%') {
      x.style.right = '0px';
      y.className = 'fa fa-times';
    }else{
      x.style.right='-100%';
      y.className='fa-solid fa-bars-staggered';
    }
}

function openCommentForm(button) {
  const commentFormContainer = button.closest('.comment-container').querySelector('.commentx');

  commentFormContainer.classList.toggle('hidden');
}
