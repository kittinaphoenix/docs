# Example with all valid objects
input_arr = [
  {"type":"t","v":[1,"Arkanoid Game"]},
  {"type":"p","v":"In this game, the player controls a paddle to bounce a ball and break bricks."},
  {"type":"t","v":[2,"Gameplay"]},
  {"type":"p","v":"Move the paddle left and right to bounce the ball and break bricks. If the ball falls below the paddle, you lose a life. You have three lives."},
  {"type":"t","v":[2,"Controls"]},
  {"type":"ta","v":{
    "h":["Key", "Action"],
    "r":[
      ["Left arrow", "Move paddle left"],
      ["Right arrow", "Move paddle right"]
    ]
  }},
  {"type":"t","v":[2,"Scoring"]},
  {"type":"p","v":"Points are awarded for each brick broken, and bonus points are awarded for breaking multiple bricks with a single ball."},
  {"type":"t","v":[2,"Levels"]},
  {"type":"p","v":"There are three levels in the game, with increasing difficulty and a different arrangement of bricks."},
  {"type":"t","v":[2,"Winning the Game"]},
  {"type":"p","v":"The game is won when all bricks have been broken."},
  {"type":"t","v":[2,"Losing the Game"]},
  {"type":"p","v":"The game is lost when all lives have been lost."},
  {"type":"s","v":"// Code for the Arkanoid game goes here"}
]

def generate_html(input_arr):
    output_str = '<div class="container mt-5 row offset-1 col-10">\n'
    for obj in input_arr:
        if 'type' not in obj or 'v' not in obj:
            return {"success": False, "error": "Input format is invalid."}
        if obj['type'] == 't':
            if not isinstance(obj['v'], list) or len(obj['v']) != 2 or not isinstance(obj['v'][0], int) or not isinstance(obj['v'][1], str):
                return {"success": False, "error": "Invalid input format for title object."}
            output_str += f'<h{obj["v"][0]} class="mb-4 text-center">{obj["v"][1]}</h{obj["v"][0]}>\n'
        elif obj['type'] == 'ta':
            if not isinstance(obj['v'], dict) or 'h' not in obj['v'] or 'r' not in obj['v'] or not isinstance(obj['v']['h'], list) or not isinstance(obj['v']['r'], list):
                return {"success": False, "error": "Invalid input format for table object."}
            for header in obj['v']['h']:
                if not isinstance(header, str):
                    return {"success": False, "error": "Invalid input format for table header."}
            for row in obj['v']['r']:
                if not isinstance(row, list):
                    return {"success": False, "error": "Invalid input format for table row."}
                for col in row:
                    if not isinstance(col, str):
                        return {"success": False, "error": "Invalid input format for table cell."}
            output_str += '<table class="table">\n<thead>\n<tr>\n'
            for header in obj['v']['h']:
                output_str += f'<th class="text-center">{header}</th>\n'
            output_str += '</tr>\n</thead>\n<tbody>\n'
            for row in obj['v']['r']:
                output_str += '<tr>\n'
                for col in row:
                    output_str += f'<td class="text-center">{col}</td>\n'
                output_str += '</tr>\n'
            output_str += '</tbody>\n</table>\n'
        elif obj['type'] == 's':
            if not isinstance(obj['v'], str):
                return {"success": False, "error": "Invalid input format for code object."}
            output_str += f'<pre><code>{obj["v"]}</code></pre>\n'
        elif obj['type'] == 'p':
            if not isinstance(obj['v'], str):
                return {"success": False, "error": "Invalid input format for paragraph object."}
            output_str += f'<p>{obj["v"]}</p>\n'
        else:
            return {"success": False, "error": f"Invalid object type '{obj['type']}'."}
    output_str += '</div>'
    return {"success": True, "html": output_str}

# Generate the HTML
result = generate_html(input_arr)

if result["success"]:
    # Output the generated HTML
    print(result["html"])
else:
    # Output the error message
    print(result["error"])