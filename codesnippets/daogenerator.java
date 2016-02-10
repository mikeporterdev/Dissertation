Schema schema = new Schema(3, "com.michael.kidquest.greendao.model");

Entity userDetails = schema.addEntity("Character");
userDetails.addIdProperty();
userDetails.addStringProperty("name").notNull();
userDetails.addIntProperty("level").notNull();
userDetails.addStringProperty("parentPin").notNull();