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

const opencomments=()=>{
    var x=document.getElementById('comments')
    x.style.display=block;
}