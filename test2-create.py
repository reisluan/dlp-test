from collections import deque

elves_energy = deque([int(num) for num in input().split()])
num_materials_in_box = deque([int(num) for num in input().split()])

made_toys = 0
used_energy = 0
counter = 1

while True:
    if not elves_energy:
        break
    if not num_materials_in_box:
        break

    current_elf_energy = elves_energy[0]
    if current_elf_energy < 5:
        elves_energy.popleft()
        continue
    current_num_materials = num_materials_in_box[-1]

    if current_elf_energy >= current_num_materials:
        if counter % 3 == 0:
            if current_elf_energy >= 2 * current_num_materials:
                current_num_materials = 2 * current_num_materials
                made_toys += 1
            else:
                current_elf_energy *= 2
                elves_energy.popleft()
                elves_energy.append(current_elf_energy)
                counter += 1
                continue
        if counter % 5 == 0:
            energy_left = current_elf_energy - current_num_materials
            used_energy += current_num_materials
            elves_energy.popleft()
            elves_energy.append(energy_left)
            num_materials_in_box.pop()
            if counter % 3 == 0:
                made_toys -= 1
            counter += 1
            continue
        energy_left = current_elf_energy - current_num_materials
        used_energy += current_num_materials
        made_toys += 1
        elves_energy.popleft()
        elves_energy.append(energy_left + 1)
        num_materials_in_box.pop()
        counter += 1
    else:
        current_elf_energy *= 2
        elves_energy.popleft()
        elves_energy.append(current_elf_energy)
        counter += 1

print(f"Toys: {made_toys}")
print(f"Energy: {used_energy}")

if elves_energy:
    print(f"Elves left: {', '.join([str(el) for el in elves_energy])}")
else:
    print(f"Boxes left: {', '.join([str(el) for el in num_materials_in_box])}")