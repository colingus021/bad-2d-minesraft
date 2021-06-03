namespace SpriteKind {
    export const Enemy2 = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (steve.vy == 0) {
        steve.vy = -200
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`lava`, function (sprite, location) {
    info.changeLifeBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`play2`, function (sprite, location) {
    tiles.setTilemap(tilemap`level7`)
    scene.setBackgroundColor(9)
    steve = sprites.create(assets.image`steve`, SpriteKind.Player)
    steve.ay = 500
    controller.moveSprite(steve, 150, 0)
    scene.cameraFollowSprite(steve)
    mouse_button.destroy()
    info.setLife(3)
    myEnemy2 = sprites.create(assets.image`grim reeper`, SpriteKind.Enemy)
    tiles.placeOnRandomTile(myEnemy2, assets.tile`test`)
    myEnemy2.follow(steve, 20)
    info.setScore(0)
    myEnemy1 = sprites.create(assets.image`duck`, SpriteKind.Enemy2)
    myEnemy1.follow(steve, 30)
    tiles.placeOnRandomTile(myEnemy1, assets.tile`duck1`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`under water`, function (sprite, location) {
    if (controller.A.isPressed()) {
        steve.vy = -150
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`play`, function (sprite, location) {
    scene.setBackgroundColor(9)
    tiles.setTilemap(tilemap`level1`)
    steve = sprites.create(assets.image`steve`, SpriteKind.Player)
    steve.ay = 500
    controller.moveSprite(steve, 150, 0)
    scene.cameraFollowSprite(steve)
    mouse_button.destroy()
    info.setLife(3)
    myEnemy2 = sprites.create(assets.image`grim reeper`, SpriteKind.Enemy)
    tiles.placeOnRandomTile(myEnemy2, assets.tile`test`)
    myEnemy2.follow(steve, 20)
    info.setScore(0)
    myEnemy1 = sprites.create(assets.image`duck`, SpriteKind.Enemy2)
    myEnemy1.follow(steve, 30)
    tiles.placeOnRandomTile(myEnemy1, assets.tile`duck1`)
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    tiles.setTilemap(tilemap`main menu`)
    scene.setBackgroundColor(13)
    mouse_button = sprites.create(assets.image`mouse button`, SpriteKind.Player)
    controller.moveSprite(mouse_button)
    steve.destroy()
})
info.onLifeZero(function () {
    steve.destroy()
    picture = sprites.create(assets.image`picture`, SpriteKind.Projectile)
    assets.image`picture`.fill(info.score())
    info.startCountdown(0)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`p`, function (sprite, location) {
    scene.setBackgroundColor(9)
    tiles.setTilemap(tilemap`level7`)
    steve = sprites.create(assets.image`steve`, SpriteKind.Player)
    steve.ay = 500
    controller.moveSprite(steve, 150, 0)
    scene.cameraFollowSprite(steve)
    mouse_button.destroy()
    info.setLife(3)
    for (let value of tiles.getTilesByType(assets.tile`test`)) {
        myEnemy2 = sprites.create(assets.image`grim reeper`, SpriteKind.Enemy)
        tiles.placeOnTile(myEnemy2, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    myEnemy2.follow(steve, 20)
    info.setScore(0)
    for (let value of tiles.getTilesByType(assets.tile`duck1`)) {
        myEnemy1 = sprites.create(assets.image`duck`, SpriteKind.Enemy2)
        tiles.placeOnTile(myEnemy1, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    myEnemy1.follow(steve, 30)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy2, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    myEnemy1.destroy()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`nether portll`, function (sprite, location) {
    tiles.setTilemap(tilemap`level0`)
    scene.setBackgroundColor(4)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    myEnemy2.destroy()
})
let picture: Sprite = null
let myEnemy1: Sprite = null
let myEnemy2: Sprite = null
let steve: Sprite = null
let mouse_button: Sprite = null
tiles.setTilemap(tilemap`main menu`)
scene.setBackgroundColor(13)
mouse_button = sprites.create(assets.image`mouse button`, SpriteKind.Player)
controller.moveSprite(mouse_button)
scene.cameraFollowSprite(mouse_button)
