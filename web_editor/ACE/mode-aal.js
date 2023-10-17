    define("ace/mode/aal",function(require, exports, module) {
        var oop = require("ace/lib/oop");
        var TextMode = require("ace/mode/text").Mode;
        var AALHighlightRules = require("aal_highlight_rules").AALHighlightRules;

        var Mode = function() {
            this.HighlightRules = AALHighlightRules;
        };
        oop.inherits(Mode, TextMode);

        (function() {
            this.$id = "ace/mode/aal";
        }).call(Mode.prototype);

        exports.Mode = Mode;
    });
