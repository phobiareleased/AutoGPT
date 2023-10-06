import os

import uvicorn
from dotenv import load_dotenv

import forge.sdk.forge_log

LOG = forge.sdk.forge_log.ForgeLogger(__name__)


logo = """\n\n
          .---.                                                
          |   |/|              __.....__                       
          |   |||          .-''         '.                     
          |   |||         /     .-''"'-.  `. .-,.--.      .|   
    __    |   |||  __    /     /________\   \|  .-. |   .' |_  
 .:--.'.  |   |||/'__ '. |                  || |  | | .'     | 
/ |   \ | |   ||:/`  '. '\    .-------------'| |  | |'--.  .-' 
`" __ | | |   |||     | | \    '-.____...---.| |  '-    |  |   
 .'.''| | |   |||\    / '  `.             .' | |        |  |   
/ /   | |_'---'|/\'..' /     `''-...... -'   | |        |  '.' 
\ \._,\ '/     '  `'-'`                      |_|        |   /  
 `--'  `"_________   _...._                             `'-'   
  .--./) \        |.'      '-.                                 
 /.''\\   \        .'```'.    '.     .|                        
| |  | |   \      |       \     \  .' |_                       
 \`-' /     |     |        |    |.'     |                      
 /("'`      |      \      /    .'--.  .-'                      
 \ '---.    |     |\`'-.-'   .'    |  |                        
  /'""'.\   |     | '-....-'`      |  |                        
 ||     || .'     '.               |  '.'                      
 \'. __//'-----------'             |   /                       
  `'---'                           `'-'                                                            
\n"""

if __name__ == "__main__":
    print(logo)
    port = os.getenv("PORT", 8000)
    LOG.info(f"Agent server starting on http://localhost:{port}")
    load_dotenv()
    forge.sdk.forge_log.setup_logger()

    uvicorn.run(
        "forge.app:app", host="localhost", port=port, log_level="error", reload=True
    )
