define("aal_highlight_rules", function (require, exports, module) {
    var oop = require("ace/lib/oop");
    var TextHighlightRules = require("ace/mode/text_highlight_rules").TextHighlightRules;

    var AALHighlightRules = function () {
        this.$rules = {
            start: [
                {
                    token: "comment",
                    regex: "\\*\\w+\\s+(?=:)",
                },
                {
                    token: "keyword",
                    regex: "\\*(LOAD|ADD|SUB|MULT|DIV)\\b",
                },
                {
                    token: "keyword",
                    regex: "(STORE|BG|BE|BL|BU|READ|PRINT|DC|END)\\b",
                },
                {
                    token: "constant.numeric",
                    regex: "\\d+",
                },
                // Add more rule definitions for your language here
            ],
        };
    };

    oop.inherits(AALHighlightRules, TextHighlightRules);
    exports.AALHighlightRules = AALHighlightRules;
});
