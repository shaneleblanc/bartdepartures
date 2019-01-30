

let data = msg.payload['root']['station'][0]['etd'];
let times = "";
for(let i=0;i<=data.length;i++){
    let item = data[i];
    let destination = item['destination'];
    let trains = [];
    let est = item['estimate']
    for (let e=0;e<=est.length;i++){
        let eitem = est[e];
        trains.push(eitem['minutes'] + 'minutes');
    }
    times.push(destination + trains.join(', '));
}
return times;