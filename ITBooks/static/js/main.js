function addToCart(id, name, donGia) {
    fetch('/api/cart', {
        'method': 'post',
        'body': JSON.stringify({
            "id": id,
            "name": name,
            "donGia": donGia,
        }),
        'headers': {
            'Context-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        var cart = document.getElementById("cart-info");
        cart.innerText = `${data.total_quantity} - ${data.total_amount} VNĐ`;
        console.info(data);
    }).catch(err => {
        console.log(err);
    });

    // promise --> await/async
}

function pay() {
    fetch('/api/pay', {
        method: 'post',
        headers: {
            'Context-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        alert(data.message);
        location.reload();
    }).catch(err => {
        location.href = '/loginuser?next=/payment';
    });
}

// dùng để add các sản phẩm khách hàng mua
function addToSell() {
    id = document.getElementById("idsach").value;
    fetch('/api/sellcart', {
        'method': "post",
        'body': JSON.stringify({
            "id": id
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        console.info(data);
        location.reload();
//
        var value = parseInt(document.getElementById(id ).value) ;
        document.getElementById(id ).value = value + 1;
    }).catch(err => {
        console.log(err);
    })

    // promise --> await/async
}
