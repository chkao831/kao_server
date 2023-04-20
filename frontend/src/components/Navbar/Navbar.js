import {  Toolbar, Grow, Grid, AppBar, Typography, Card, CardActions, CardMedia, CssBaseline } from "@material-ui/core";
import {PhotoCamera} from '@material-ui/icons'
import useStyles from './styles';



const Navbar = () => {
    const classes = useStyles();
    return (
        <>
            <CssBaseline />
            <AppBar position="relative">
                <Toolbar>
                    <PhotoCamera />
                    <Typography variant="h6"> Photo Album</Typography>
                </Toolbar>
            </AppBar>
        </>
        )
                
}

export default Navbar;
//水 PNG圖片素材由hidungjeruk设计 https://zh.pngtree.com/freepng/cute-little-water-monster-rpg_9039516.html?sol=downref&id=bef