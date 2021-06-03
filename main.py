znamespace
SpriteKind
Enemy2 = SpriteKind.create()

def on_a_pressed():
    if steve.vy == 0:
        steve.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        lava
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    global steve, myEnemy2, myEnemy1
    tiles.set_tilemap(tilemap("""
        level3
    """))
    scene.set_background_color(9)
    steve = sprites.create(assets.image("""
        steve
    """), SpriteKind.player)
    steve.ay = 500
    controller.move_sprite(steve, 150, 0)
    scene.camera_follow_sprite(steve)
    mouse_button.destroy()
    info.set_life(3)
    myEnemy2 = sprites.create(assets.image("""
        grim reeper
    """), SpriteKind.enemy)
    tiles.place_on_random_tile(myEnemy2, assets.tile("""
        test
    """))
    myEnemy2.follow(steve, 20)
    info.set_score(0)
    myEnemy1 = sprites.create(assets.image("""
        duck
    """), SpriteKind.Enemy2)
    myEnemy1.follow(steve, 30)
    tiles.place_on_random_tile(myEnemy1, assets.tile("""
        duck1
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        play2
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    if controller.A.is_pressed():
        steve.vy = -150
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        under water
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite, location):
    global steve, myEnemy2, myEnemy1
    scene.set_background_color(9)
    tiles.set_tilemap(tilemap("""
        level1
    """))
    steve = sprites.create(assets.image("""
        steve
    """), SpriteKind.player)
    steve.ay = 500
    controller.move_sprite(steve, 150, 0)
    scene.camera_follow_sprite(steve)
    mouse_button.destroy()
    info.set_life(3)
    myEnemy2 = sprites.create(assets.image("""
        grim reeper
    """), SpriteKind.enemy)
    tiles.place_on_random_tile(myEnemy2, assets.tile("""
        test
    """))
    myEnemy2.follow(steve, 20)
    info.set_score(0)
    myEnemy1 = sprites.create(assets.image("""
        duck
    """), SpriteKind.Enemy2)
    myEnemy1.follow(steve, 30)
    tiles.place_on_random_tile(myEnemy1, assets.tile("""
        duck1
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        play
    """),
    on_overlap_tile4)

def on_menu_pressed():
    global mouse_button
    tiles.set_tilemap(tilemap("""
        main menu
    """))
    scene.set_background_color(13)
    mouse_button = sprites.create(assets.image("""
        mouse button
    """), SpriteKind.player)
    controller.move_sprite(mouse_button)
    steve.destroy()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_life_zero():
    global picture
    steve.destroy()
    picture = sprites.create(assets.image("""
        picture
    """), SpriteKind.projectile)
    assets.image("""
        picture
    """).fill(info.score())
    info.start_countdown(0)
info.on_life_zero(on_life_zero)

def on_overlap_tile5(sprite, location):
    global steve, myEnemy2, myEnemy1
    scene.set_background_color(9)
    tiles.set_tilemap(tilemap("""
        level7
    """))
    steve = sprites.create(assets.image("""
        steve
    """), SpriteKind.player)
    steve.ay = 500
    controller.move_sprite(steve, 150, 0)
    scene.camera_follow_sprite(steve)
    mouse_button.destroy()
    info.set_life(3)
    myEnemy2 = sprites.create(assets.image("""
        grim reeper
    """), SpriteKind.enemy)
    tiles.place_on_random_tile(myEnemy2, assets.tile("""
        test
    """))
    myEnemy2.follow(steve, 20)
    info.set_score(0)
    myEnemy1 = sprites.create(assets.image("""
        duck
    """), SpriteKind.Enemy2)
    myEnemy1.follow(steve, 30)
    tiles.place_on_random_tile(myEnemy1, assets.tile("""
        duck1
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        p
    """),
    on_overlap_tile5)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    myEnemy1.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Enemy2, on_on_overlap)

def on_overlap_tile6(sprite, location):
    tiles.set_tilemap(tilemap("""
        level0
    """))
    scene.set_background_color(4)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        nether portll
    """),
    on_overlap_tile6)

def on_on_overlap2(sprite, otherSprite):
    info.change_life_by(-1)
    myEnemy2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

picture: Sprite = None
myEnemy1: Sprite = None
myEnemy2: Sprite = None
steve: Sprite = None
mouse_button: Sprite = None
tiles.set_tilemap(tilemap("""
    main menu
"""))
scene.set_background_color(13)
mouse_button = sprites.create(assets.image("""
    mouse button
"""), SpriteKind.player)
controller.move_sprite(mouse_button)
scene.camera_follow_sprite(mouse_button)