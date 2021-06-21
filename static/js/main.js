var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.object
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		// console.log('USER:', user)

		const sendData = updateUserOrder(productId, action)

	})
}

var updateQty = document.getElementsByClassName('update-Qty')

for (i = 0; i < updateQty.length; i++) {
	updateQty[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		// console.log('USER:', user)

		const sendData = updateUserOrder(productId, action)

	})
}



function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
			return response.json();
		 })
		.then((data) => {
			location.reload()
		 });
		
}

$(window).load(function () {
	$(".trigger_popup_fricc").click(function(){
	   $('.hover_bkgr_fricc').show();
	});
	$('.hover_bkgr_fricc').click(function(){
		$('.hover_bkgr_fricc').hide();
	});
	$('.popupCloseButton').click(function(){
		$('.hover_bkgr_fricc').hide();
	});
});
  
