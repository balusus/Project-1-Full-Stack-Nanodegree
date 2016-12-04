import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

wall_e = media.Movie("WALL-E",
                        "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                        "https://www.youtube.com/watch?v=alIq_wG9FNk")

finding_nemo = media.Movie("Finding Nemo",
                        "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.",
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                        "https://www.youtube.com/watch?v=bMtzgW-FVLY")

shrek = media.Movie("Shrek",
                        "After his swamp is filled with magical creatures, an ogre agrees to rescue a princess for a villainous lord in order to get his land back.",
                        "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
                        "https://www.youtube.com/watch?v=ezdEomjFw4Q")

ratatouille = media.Movie("Ratatouille",
                        "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=niD-jahFURU")

mulan = media.Movie("Mulan",
                        "To save her father from death in the army, a young maiden secretly goes in his place and becomes one of China's greatest heroines in the process.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",
                        "https://www.youtube.com/watch?v=wAbGAkkOgcM")

movies = [toy_story, wall_e, finding_nemo, shrek, ratatouille, mulan ]
fresh_tomatoes.open_movies_page(movies)
