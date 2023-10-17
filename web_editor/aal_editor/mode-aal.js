define("ace/mode/aal", function (require, exports, module) {
    var oop = require("ace/lib/oop");
    var TextMode = require("ace/mode/text").Mode;
    var AALHighlightRules = require("aal_highlight_rules").AALHighlightRules;

    var Mode = function () {
        this.HighlightRules = AALHighlightRules;
    };
    oop.inherits(Mode, TextMode);

    (function () {
        this.$id = "ace/mode/aal";
    }).call(Mode.prototype);

    // 定义 AAL 指令作为关键字
    var aalKeywords = [
        "LOAD",
        "STORE",
        "ADD",
        "SUB",
        "MULT",
        "DIV",
        "BG",
        "BE",
        "BL",
        "BU",
        "READ",
        "PRINT",
        "DC",
        "END"
    ];

    // 创建关键字映射
    var keywordMap = {};
    aalKeywords.forEach(function (keyword) {
        keywordMap[keyword] = "ace_keyword";
    });
    this.$highlightRules.setKeywords(keywordMap);
    exports.Mode = Mode;
});
