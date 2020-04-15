# Print out all of the strings in the following array in alphabetical order, each on a separate line.
words = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']


words = sorted(words)
print(*words, sep = '\n')