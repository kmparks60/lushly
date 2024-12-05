
import * as React from 'react';
import Button from '@mui/material/Button';
import HomeIcon from '@mui/icons-material/Home'
import Card from '@mui/material/Card';
import Toolbar from '@mui/material/Toolbar';
import {Link} from 'react-router-dom';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart'
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import EditIcon from '@mui/icons-material/Edit';
import AppBar from '@mui/material/AppBar'
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import lushly from './lushly.png'
import CardMedia from '@mui/material/CardMedia';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];

export default function Album() {
  return (
    <>
      <AppBar
        position="static"
        color="default"
        elevation={0}
        sx={{ borderBottom: (theme) => `1px solid ${theme.palette.divider}` }}
      >
        <Toolbar sx={{ flexWrap: 'wrap' }}>
          <Button><Link to='/'><HomeIcon/></Link></Button>
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
      <main className='bg-slate-400'>
        <Box className='bg-white pt-2 pb-6'>
          <Container maxWidth="sm">
            <Typography
              className='text-green-600'
              component="h1"
              variant="h2"
              align="center"
              color="text.success.main"
              gutterBottom
            >
              Lushly Products
            </Typography>
            <Typography variant="h5" align="center" 
            color="text.secondary" paragraph>
              Welcome to the Lushly Product Page
            </Typography>
          </Container>
        </Box>
        <Container sx={{ py: 8 }} maxWidth="md">
          <Grid container spacing={4}>
            {cards.map((card) => (
              <Grid item key={card} xs={12} sm={6} md={4}>
                <Card
                  sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
                >
                  <CardMedia
                    component="div"
                    sx={{
                      pt: '56.25%',
                    }} />
                    <img alt='company' src={lushly} /> 
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="h5" component="h2">
                      Product
                    </Typography>
                    <Typography>
                      Info on Lushly Products.
                    </Typography>
                  </CardContent>
                  <CardActions>
                    <Button size="small"><EditIcon/></Button>
                    <Button size="extra small"><AddShoppingCartIcon/></Button>
                    <Button></Button>
                  </CardActions>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Container>
      </main>
    </>
  );
}