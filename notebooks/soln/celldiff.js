%%javascript

// this is a small example of javascript extension that can be used to add
// metadata attached to each cell.  Using the %%javascript magic to do it is
// just an example that should not be used in production code.  You should use
// custom.js to asynchroously load you extension and make it listen to the
// correct IPython event to trigger your logic

// this in particular will register a dropdown menu with value Easy/Medium/Hard
// you can attach to each cell. We will uses thoses data in nbconvert
// templates.  to make the cells of different colors.


var CellToolbar = IPython.CellToolbar

var select_type = CellToolbar.utils.select_ui_generator([
             ["<None>"       , "<None>"             ],
             ["Easy"         , "Easy"         ],
             ["Medium"       , "Medium"       ],
             ["Hard"         , "Hard"         ],
         ],
         // setter
         function(cell, value){
             // we check that the `example` namespace exist and create it if needed
             if (cell.metadata.example == undefined){cell.metadata.example = {}}
             // set the value
             cell.metadata.example.difficulty = value
             },
         //getter
         function(cell){ var ns = cell.metadata.example;
             return (ns == undefined)? undefined: ns.difficulty
             }
)
    
CellToolbar.register_callback('difficulty.select', select_type);
CellToolbar.register_preset('difficulty', ['difficulty.select']);
