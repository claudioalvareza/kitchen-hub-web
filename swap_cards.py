import sys

def read_lines(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

def write_lines(filepath, lines):
    with open(filepath, 'w') as f:
        f.writelines(lines)

idx_lines = read_lines('/Users/claudio/.gemini/antigravity/scratch/kitchen-hub/index.html')
nunoa_lines = read_lines('/Users/claudio/.gemini/antigravity/scratch/kitchen-hub/dark-kitchen-nunoa.html')

# Extract cards from index.html (lines 194 to 284, 0-indexed: 193 to 284)
index_cards = idx_lines[193:284]

# Extract modals from index.html (lines 848 to 1207, 0-indexed: 847 to 1207)
index_modals = idx_lines[847:1207]

# Replace cards in nunoa (lines 261 to 328, 0-indexed: 260 to 328)
# Keep lines up to 260, add cards, add lines from 328 onwards
new_nunoa = nunoa_lines[:260] + index_cards + nunoa_lines[328:]

# Recalculate modal positions since lines have changed
modal_start = -1
for i, line in enumerate(new_nunoa):
    if '<div id="modal-nunoa-landing" class="modal">' in line:
        modal_start = i
        break

modal_end = -1
for i in range(modal_start, len(new_nunoa)):
    if '<!-- Kitchen Hub AI Agent Widget -->' in new_nunoa[i]:
        modal_end = i - 1
        break

while new_nunoa[modal_end].strip() == '':
    modal_end -= 1

new_nunoa2 = new_nunoa[:modal_start] + index_modals + ['\n'] + new_nunoa[modal_end+1:]

write_lines('/Users/claudio/.gemini/antigravity/scratch/kitchen-hub/dark-kitchen-nunoa.html', new_nunoa2)
print("Done")
