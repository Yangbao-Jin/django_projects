define("ace/mode/custom_highlight_rules", [], function (require, exports) {
    var oop = require("ace/lib/oop");
    var TextHighlightRules = require("ace/mode/text_highlight_rules").TextHighlightRules;

    var CustomHighlightRules = function () {
        this.$rules = {
            start: [
                {
                    token: "comment",
                    regex: "\\*\\w+\\s+(?=:)",
                    // 设置注释的颜色
                    comment: "green"
                },
                {
                    token: "keyword",
                    regex: "\\*(LOAD|ADD|SUB|MULT|DIV)\\b",
                    // 设置关键字的颜色
                    keyword: "blue"
                },
                {
                    token: "keyword",
                    regex: "(STORE|BG|BE|BL|BU|READ|PRINT|DC|END)\\b",
                    // 设置另一类关键字的颜色
                    keyword: "red"
                },
                {
                    token: "constant.numeric",
                    regex: "\\d+",
                    // 设置数字的颜色
                    constant: "purple"
                },
            ],
        };
    };
    

    oop.inherits(CustomHighlightRules, TextHighlightRules);
    exports.CustomHighlightRules = CustomHighlightRules;
});

define("ace/mode/custom", [], function (require, exports, module) {
    var oop = require("ace/lib/oop");
    var TextMode = require("ace/mode/text").Mode;
    var CustomHighlightRules = require("ace/mode/custom_highlight_rules").CustomHighlightRules;

    var Mode = function () {
        this.HighlightRules = CustomHighlightRules;
    };
    oop.inherits(Mode, TextMode);

    (function () {
        this.$id = "ace/mode/custom";
    }).call(Mode.prototype);

    exports.Mode = Mode;
});
