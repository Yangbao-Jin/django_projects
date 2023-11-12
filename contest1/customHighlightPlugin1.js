// 创建 TinyMCE 插件
tinymce.PluginManager.add('customhighlight', function(editor) {
    // 添加高亮按钮到工具栏
    editor.ui.registry.addButton('highlightcode', {
        text: 'Highlight Code',
        onAction: function() {
            // 获取编辑器内容
            // 获取编辑器内容
            var code = editor.getContent({ format: 'text' });

            // 分割代码为单行
            var lines = code.split('\n');

            // 遍历每一行代码
            for (var i = 0; i < lines.length; i++) {
                var line = lines[i];
                // 使用正则表达式匹配标签、操作码和位置
                var regex = /([A-Za-z][A-Za-z0-9]*)\s+([A-Za-z]+)\s+([A-Za-z0-9]+|= [0-9]+)/g;
                line = line.replace(regex, '<span class="label">$1</span> <span class="opcode">$2</span> <span class="location">$3</span>');

                // 将处理后的行放回原数组
                lines[i] = line;
            }

            // 重新构建编辑器内容
            var newCode = lines.join('\n');
            editor.setContent(newCode, { format: 'html' });

        },
    });

    return {
        getMetadata: function() {
            return {
                name: 'Custom Highlight Plugin',
            };
        },
    };
});
