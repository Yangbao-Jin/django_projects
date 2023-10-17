define(function(require, exports, module) {
    var oop = require("ace/lib/oop");
    var TextHighlightRules = require("ace/mode/text_highlight_rules").TextHighlightRules;

    var AALHighlightRules = function() {
        var keywordList = [
            "LOAD", "STORE", "ADD", "SUB", "MULT", "DIV", "BG", "BE", "BL", "BU",
            "READ", "PRINT", "DC", "END"
        ];

        this.$rules = {
            "start": [
                {
                    token: "label",
                    regex: "[A-Za-z][A-Za-z0-9]*\\s+"
                },
                {
                    token: "keyword",
                    regex: "\\b(" + keywordList.join("|") + ")\\b"
                },
                {
                    token: "variable",
                    regex: "[A-Za-z][A-Za-z0-9]*"
                },
                {
                    token: "number",
                    regex: "\\d+"
                },
                {
                    token: "comment",
                    regex: "//.*$"
                }
            ]
        };
    };

    oop.inherits(AALHighlightRules, TextHighlightRules);

    exports.AALHighlightRules = AALHighlightRules;
});
