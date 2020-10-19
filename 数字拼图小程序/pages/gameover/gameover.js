// pages/gameover/gameover.js
var app = getApp();
Page({

  data: {
    step:0,
    hscore : 0,
    showDialog: false
  },


  onLoad: function (options) {
    this.setData({
      step : options.step,
    })
    if (options.step < app.globalData.max) {
      getApp().globalData.max = options.step;
      this.setData({
        hscore :app.globalData.max,
      })
    }

  },

  returnGame() {
    wx.redirectTo({
      url : '../index/index'
    })
  },

})