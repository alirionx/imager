
function hello_world(){
  var newDate = new Date();
  var timeStr = newDate.toLocaleTimeString();
  alert("Hello World, it is: "+timeStr);
}


testVue = new Vue({
  el: "#test",
  data: {
    msg: "test",
    time: ""
  },
  methods: {
    update_time(){
      var newDate = new Date();
      var timeStr = newDate.toLocaleTimeString();
      this.time = timeStr;
    },
    start_timer(){
      //clearInterval(timeInter);
      this.update_time();
      this.timer = setInterval(this.update_time,1000);
    },
    stop_timer(){
      clearInterval(this.timer);
      console.log("clear");
    }
  },
  created: function(){
    console.log("test vue mounted");
    //this.start_timer();
  }
})