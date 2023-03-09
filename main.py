import logging
from nbt import nbt

def nuke_biomes(nuked_namespace: str, dimension: str , file: str | nbt.NBTFile = "./level.dat") -> nbt.NBTFile:
    if isinstance(file, str):
        logging.info(f"Getting NBTFile from '{file}'")
        nbtfile = nbt.NBTFile(file, "rb")
    elif isinstance(file, nbt.NBTFile):
        logging.info("NBTFile supplied")
        nbtfile = file
    else:
        raise TypeError(f"Expected type of 'str' or 'nbt.NBTFile', found '{type(file)}'")

    biomes_location = nbtfile["Data"]["WorldGenSettings"]["dimensions"][dimension]["generator"]["biome_source"]["biomes"]
    for index, tag in enumerate(biomes_location):
        biome = str(tag['biome']).split(":")
        logging.debug(f"Checking biome {biome}")
        if biome[0] == nuked_namespace:
            logging.debug(f"Matched biome {biome} to {nuked_namespace}. Nuking..")
            biomes_location[index].clear()

    return nbtfile

if __name__ == "__main__":
    nuke_biomes("incendium", "minecraft:the_nether").write_file("export.dat")