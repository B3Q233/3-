layui.define(function (exports) {
  // 也可以依赖其他模块
  var obj = {
    hello: function (str) {
      alert("Hello " + (str || "firstMod"));
    },
  };

  // 输出 firstMod 接口
  exports("firstMod", obj);
});
