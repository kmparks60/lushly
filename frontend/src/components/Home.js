import React from 'react';
import {Link} from 'react-router-dom';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart'
import Button from '@mui/material/Button';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

function Home() {
  return (
    <>
      <AppBar
        position="static"
        color="default"
        elevation={0}
        sx={{ borderBottom: (theme) => `1px solid ${theme.palette.divider}` }}
      >
        <Toolbar sx={{ flexWrap: 'wrap' }}>
          <Typography  className='text-green-600' variant="h6" noWrap sx={{ flexGrow: 1 }}>
            Lushly
          </Typography>
          <nav>
            <Button><Link to='/products'>Products</Link></Button>
            <Button><Link to='/login'>Login</Link></Button>
            <Button><Link to='/signup'>Sign Up</Link></Button>
            <Button><Link to='/checkout'><ShoppingCartIcon/></Link></Button>
          </nav>
        </Toolbar>
      </AppBar>
    </>
  )
}

export default Home
