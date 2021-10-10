import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MatoGrossoDoSulComponent } from './mato-grosso-do-sul.component';

describe('MatoGrossoDoSulComponent', () => {
  let component: MatoGrossoDoSulComponent;
  let fixture: ComponentFixture<MatoGrossoDoSulComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MatoGrossoDoSulComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MatoGrossoDoSulComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
