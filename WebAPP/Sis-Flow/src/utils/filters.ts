const filters = (value:string, min:string, max:string):string => {
    let myVal = parseFloat(value);
    let myMin = parseFloat(min);
    let myMax   = parseFloat(max);
    if(myVal<myMin){
        return 'low'
    }
    if(myVal>=myMin && myVal<=myMax){
        return 'ok'
    }
    if(((myVal / myMax) * 100) >= 120 ){
        return 'hihi'
    }
    return 'hi'
}



export default filters;