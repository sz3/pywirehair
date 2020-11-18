# Success code
Wirehair_Success = 0

# More data is needed to decode.  This is normal and does not indicate a failure
Wirehair_NeedMore = 1

# Other values are failure codes:

# A function parameter was invalid
Wirehair_InvalidInput = 2

# Encoder needs a better dense seed
Wirehair_BadDenseSeed = 3

# Encoder needs a better peel seed
Wirehair_BadPeelSeed = 4

# N = ceil(messageBytes / blockBytes) is too small.
# Try reducing block_size or use a larger message
Wirehair_BadInput_SmallN = 5

# N = ceil(messageBytes / blockBytes) is too large.
# Try increasing block_size or use a smaller message
Wirehair_BadInput_LargeN = 6

# Not enough extra rows to solve it, must give up
Wirehair_ExtraInsufficient = 7

# An error occurred during the request
Wirehair_Error = 8

# Out of memory
Wirehair_OOM = 9

# Platform is not supported yet
Wirehair_UnsupportedPlatform = 10

WirehairResult_Count = 11  # /* for asserts */

WirehairResult_Padding = 0x7fffffff  # /* int32_t padding */