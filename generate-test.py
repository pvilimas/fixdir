import os

dir = 'test'

# os.rmdir(dir)
# os.mkdir(dir)

for i in (1, 2, 3, 4, 5, 6):
    for j in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
        name = f'The.Sopranos.S{i}E{j:02}.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.mkv'
        os.system(f'touch "{dir}/{name}"')

print(sorted(os.listdir(dir)))