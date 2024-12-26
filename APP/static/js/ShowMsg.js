  function showError(msg) {
        layui.use('layer', function () {
            let layer = layui.layer;
            layer.msg(msg); // 默认风格
        });
    }