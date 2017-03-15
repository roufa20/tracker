import facepy
#print(facepy.utils.get_application_access_token( "742229345893184", 
#"cda21df241b6c0a6d9ab92f29a6181f7"))
tock = facepy.utils.get_extended_access_token("742229345893184|3aruXnQASWiUshvyHiUCZimpRvw",
"742229345893184", 
"cda21df241b6c0a6d9ab92f29a6181f7")
print(tock)
