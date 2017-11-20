// initialize the php parser factory class
var fs = require('fs');
var path = require('path');
var engine = require('php-parser');
var util = require('util')
 
// initialize a new parser instance
var parser = new engine({
  // some options :
  parser: {
    extractDoc: true
  },
  ast: {
    withPositions: true
  }
});
 
// Retrieve the AST from the specified source
//var eval = parser.parseEval('echo "Hello World";');
 
// Retrieve an array of tokens (same as php function token_get_all)
//var tokens = parser.tokenGetAll('<?php echo "Hello World";');
 
// Load a static file (Note: this file should exist on your computer)
var myArray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
myArray.forEach(function(value){
  var phpFile = fs.readFileSync(util.format('samples/slice%d.php', value));
 
  // Log out results
  //console.log( 'Eval parse:', eval );
  //console.log( 'Tokens parse:', tokens );
  console.log(value);
  var content = JSON.stringify(parser.parseCode(phpFile, {
    parser: {
      debug: false, 
      locations: false,
      extractDoc: false,
      suppressErrors: false
    },
    lexer: {
      all_tokens: false,
      comment_tokens: false,
      mode_eval: false,
      asp_tags: false,
      short_tags: false
    }
  }) );
  fs.writeFile(util.format('samples/slice%d.json', value), content, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
  }); 
});
