const url =  "https://gontwsqzoljbiwwxdriug7qmja0wftca.lambda-url.ap-southeast-2.on.aws/";
const visitor_counter = document.querySelector(".visitor-counter");

async function update_visitor_counter(){
    let res = await fetch(url);
    let count = await res.json();
    visitor_counter.innerHTML = `Views : ${count}`;
}

update_visitor_counter();