from nbt import nbt

def nuke_biomes(nuked_namespace: str, dimension: str , file_path: str = "./level.dat") -> None:
    nbtfile = nbt.NBTFile(file_path, "rb")
    biomes_location = nbtfile["Data"]["WorldGenSettings"]["dimensions"][dimension]["generator"]["biome_source"]["biomes"]
    for index, tag in enumerate(biomes_location):
        biome = str(tag['biome']).split(":")
        if biome[0] == nuked_namespace:
            biomes_location[index].clear()
            nbtfile.write_file("export.dat")
            # print(biomes_location[index])
            # help(nbt.TAG_Compound)
        # print(type(tag))

nuke_biomes("incendium", "minecraft:the_nether")