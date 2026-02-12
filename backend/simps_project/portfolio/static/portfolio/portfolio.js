document.addEventListener('DOMContentLoaded',()=>
{
    const deleteButtons = document.querySelectorAll('.delete_btn');
    
    deleteButtons.forEach(button =>{
        button.addEventListener('click', function(){
            const portfolioId = this.getAttribute('data-portfolio-id');
            const url = this.getAttribute('data-url');
            console.log('Portfolio ID:', portfolioId);  
            console.log('Type:', typeof portfolioId);   
            if (!portfolioId) {
                alert('Error: No portfolio ID found!');
                return;
            }
            if(!confirm('Are you sure you want to delete this holding?')){
                return;
            }
            fetch(url,{
                method:'POST',
                headers: {
                    'Content-Type':'application/json',
                    'X-CSRFToken':getCookie('csrftoken')
                }
            })
            .then(response=>{
                console.log('Status:',response.status);
                console.log('Content-Type:',response.headers.get('content-type'));
                return response.text();
            })
            .then(text =>{
                console.log('Response:',text);
                try{
                const data = JSON.parse(text);
                if(data.redirect){
                    window.location.href = data.redirect;
                    return;
                }
                if(data.success){
                    const row = document.getElementById(`holding-${portfolioId}`);

                    const invest = parseFloat(row.dataset.invest);
                    const current = parseFloat(row.dataset.current);
                    const pl = parseFloat(row.dataset.pl);

                    let totalInvest = parseFloat(document.getElementById('total-invest').dataset.value);
                    let totalCurrent = parseFloat(document.getElementById('total-current').dataset.value);
                    let totalPL = parseFloat(document.getElementById('total-pl').dataset.value);

                    totalInvest-=invest;
                    totalCurrent-= current;
                    totalPL -= pl;
                    let totalPercent = 0;
                    if(totalInvest!= 0){
                        totalPercent = ((totalCurrent-totalInvest)*100)/totalInvest;
                    }
                    
                    const investEl = document.getElementById('total-invest');
                    const currentEl = document.getElementById('total-current');
                    const totalEl = document.getElementById('total-pl');
                    const totalperEl = document.getElementById('total-percent');
                    
                    //Removing colors to change when deleted again
                    totalEl.classList.remove('text-emerald-500', 'text-rose-500');
                    totalperEl.classList.remove('text-emerald-500', 'text-rose-500');
                    
                    if(totalPL >=0){
                        totalEl.classList.add('text-emerald-500');
                    }
                    else{
                        totalEl.classList.add('text-rose-500');
                    }

                    if (totalPercent>=0){
                        totalperEl.classList.add('text-emerald-500');
                    }
                    else{
                        totalperEl.classList.add('text-rose-500');
                    }

                    investEl.dataset.value =  totalInvest.toFixed(2);
                    investEl.innerText = '$'+ totalInvest.toFixed(2);
                    currentEl.dataset.value = totalCurrent.toFixed(2);
                    currentEl.innerText = '$'+ totalCurrent.toFixed(2);
                    totalEl.dataset.value = totalPL.toFixed(2);
                    totalEl.innerText = '$'+ totalPL.toFixed(2);
                    totalperEl.dataset.value = totalPercent.toFixed(2);
                    totalperEl.innerText =  totalPercent.toFixed(2) + '%';
                    
                    row.remove();

                    alert('Holding deleted successfully!');
                }
                else{
                    alert('Error: '+data.error);
                }}
                catch(e){
                    console.error('Failed to parse JSON:',e);
                    console.error('Response was:',text);
                    alert('Invalid Response from the server');
                }
            })

            .catch(error => {
                console.error('Error:',error);
                alert('Deletion failed. Please try again.');
            });
        });
    });
});

function getCookie(name){
    let cookieVal = null;
    if(document.cookie && document.cookie!==''){
        const cookies = document.cookie.split(';');
        for (let i = 0;i<cookies.length;i++){
            const cookie = cookies[i].trim();
            if(cookie.substring(0,name.length +1)=== (name + '=')){
                cookieVal = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieVal;
}