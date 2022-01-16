fetch('http://127.0.0.1:5000/dodouid').then(
    resp => {
        return resp.json()
    }
).then(
    data => {
        let root = document.getElementById('root')
        root.innerText = JSON.stringify(data)
    }
)